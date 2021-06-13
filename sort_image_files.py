import calendar
import glob
import os
import piexif


def build_file_list(source_folder_path, file_match_pattern="*.*"):
    """
    Builds a list of files, using the provided path, and file match pattern.

    :param source_folder_path:
    :param file_match_pattern:
    :return:
    """

    return glob.glob(os.path.join(source_folder_path, file_match_pattern))


def sort_files(source_folder_path, destination_folder_path, file_match_pattern, sorting_scheme):
    """
    Iterate through the files, in the provided path, and attempt to sort them using the specified sorting scheme.

    :param source_folder_path:
    :param destination_folder_path:
    :param file_match_pattern:
    :param sorting_scheme:
    :return:
    """

    # Builds the list of files to sort, using the provided path, and file match pattern
    file_list = build_file_list(source_folder_path, file_match_pattern)

    # Attempts to sort the files, in the provided list.
    results = sorting_scheme(file_list, destination_folder_path)

    return results


def compute_hierarchical_path_components(datetime_string):
    """
    Computes the hierarchical path components, from the provided datetime string, in the following format:

    ['YYYY', 'MM - Month', 'DD']

    YYYY - four digit year
    MM - month number (zero padded)
    Month - month name
    DD - day number (zero padded)

    Example: ('2020:01:22 18:00:00')

    ['2020', '01 - January', '22']

    :param datetime_string: string
    :return: string
    """

    path_components = []

    # Confirms that a datetime string has been provided.
    if datetime_string:

        # Extracts the date components from the provided string.
        date_parts = datetime_string.strip().split(" ")[0]
        date_parts = date_parts.split(":")

        # Confirms that there are 3 date components (year, month, day).
        if len(date_parts) == 3:

            # Unpacks the year, month, and day from the date components.
            year = date_parts[0]
            month_number = date_parts[1]
            day = date_parts[2]

            # Confirms that each of the date components are valid
            if is_year_valid(year) and is_month_valid(month_number) and is_day_valid(day):

                # Constructs the path, from the provided date components.
                month_name = calendar.month_name[int(month_number)]
                month = "{} - {}".format(month_number, month_name)
                path_components = [year, month, day]

    return path_components


def is_year_valid(year):
    """
    Determines whether the provided year is valid. In order for it to be considered valid, it must meet the following
    criteria:

    1) is 4 digits in length
    2) is a valid base-10 numeric value

    :param year:
    :return:
    """

    valid = True if len(year) == 4 and year.isnumeric() else False

    return valid


def is_month_valid(month):
    """
    Determines whether the provided month is valid. In order for it to be considered valid, it must meet the following
    criteria:

    1) is 2 digits in length
    2) is between 01 and 12 (inclusive)
    3) is a valid base-10 numeric value

    :param month:
    :return:
    """

    valid_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    valid = True if month in valid_months else False

    return valid


def is_day_valid(day):
    """
    Determines whether the provided day is valid. In order for it to be considered valid, it must meet the following
    criteria:

    1) is 2 digits in length
    2) is between 01 and 31 (inclusive)
    3) is a valid base-10 numeric value

    :param day:
    :return:
    """

    valid = False

    if len(day) == 2 and day.isnumeric():
        day_int = int(day)
        if day_int > 0 and day_int < 32:
            valid = True

    return valid


def get_creation_date_from_file(file_path):
    """
    Attempts to determine the image creation date, from the EXIF metadata in the provided file.

    :param file_path:
    :return:
    """

    # Attempts to retrieve the DateTimeOriginal property, from the EXIF metadata.
    try:
        metadata = piexif.load(file_path)
        creation_date = metadata['Exif'][piexif.ExifIFD.DateTimeOriginal].decode("utf-8")

    # Sets the creation date to an empty string, if it cannot be retrieved from the EXIF metadata.
    except Exception as e:
        creation_date = ""

    return creation_date


def check_or_create_path(base_path, subfolder_components):
    """
    Checks to see if the folder that is specified (by joining the provided base path and subfolder components)
    exists. If it doesn't, then each of the missing subfolders are created.

    :param base_path:
    :param subfolder_components:
    :return:
    """

    # Checks to see if the entire path is valid.
    try:
        path = os.path.join(base_path, *subfolder_components)
        os.stat(path)
        exists = True

    # If the path doesn't exist, then recursively create each of the missing folders.
    except FileNotFoundError:

        # Checks to see if the parent folder of the specified path is valid.
        exists = check_or_create_path(base_path, subfolder_components[:-1])
        path = os.path.join(base_path, *subfolder_components)

        # Attempts to create the folder.
        try:
            os.mkdir(path)

        except FileNotFoundError:
            exists = False

    return exists


def sort_hierarchical_by_date(file_list, destination_base_path):
    """
    Iterate through the provided list of files, and sort them into a hierarchical folder structure, in the
    following format:

    destination_base_path/YYYY/MM - Month/DD

    YYYY - four digit year
    MM - month number (zero padded)
    Month - month name
    DD - day number (zero padded)

    Example: (January 22, 2020)

    /destination_base_path/2020/01 - January/22

    :param file_list:
    :param destination_base_path:
    :return:
    """

    results = {"success": [], "failure": {}}

    # Sets the destination path to the current working directory, if one hasn't be specified.
    if not destination_base_path:
        destination_base_path = os.getcwd()
        print("No destination path specified. Using current directory as default.")

    # Visits each file, in the provided list, and moves it to the computed destination path, based on the date that
    # is specified in the EXIF metadata.
    for file_path in file_list:
        print("Inspecting file: {}".format(file_path))

        # Attempts to extract the creation data from the EXIF metadata.
        creation_date = get_creation_date_from_file(file_path)

        if creation_date == "":
            result = "Unable to extract creation date from EXIF metadata."
            results['failure'][file_path] = result
            print("\t{}".format(result))

        else:
            computed_destination_folder = compute_hierarchical_path_components(creation_date)
            filename = os.path.split(file_path)[1]
            full_destination_path = os.path.join(destination_base_path, *computed_destination_folder, filename)

            # Attempts to move the file into the appropriate folder.
            try:
                print("\tMoving to: {}".format(full_destination_path))

                # Assures that the necessary destination folder structure exists
                exists = check_or_create_path(destination_base_path, computed_destination_folder)
                if exists:

                    # Moves the file to the destination in the hierarchical folder structure.
                    # TODO: check to see if file already exists (will currently overwrite)
                    os.rename(file_path, full_destination_path)
                    results['success'].append(file_path)

                else:
                    result = "Unable to create the destination folder"
                    results['failure'][file_path] = result
                    print("\t{}".format(result))

            except Exception as e:
                result = "Error moving file: {}".format(e)
                results['failure'][file_path] = result
                print("\t{}".format(result))

    return results


if __name__ == '__main__':

    # TODO: add support for parsing command line arguments to specify source, and destination paths
    source_path = os.getcwd()
    destination_path = os.getcwd()
    filename_match_pattern = "*.*"
    scheme = sort_hierarchical_by_date

    # Sorts the files, based on the provided parameters.
    sort_files(source_path, destination_path, filename_match_pattern, scheme)
