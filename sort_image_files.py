import calendar
import os
import piexif


def sort_files(source_path, destination_path, sorting_scheme):
    """
    Iterate through the files, in the provided path, and attempt to sort them using the specified sorting scheme.

    :param source_path:
    :param destination_path:
    :param sorting_scheme:
    :return:
    """

    sorting_scheme(source_path, destination_path)


def compute_hierarchical_path(datetime_string):
    """
    Computes the hierarchical path, from the provided datetime string, in the following format:

    destination_path/YYYY/MM - Month/DD

    YYYY - four digit year
    MM - month number (zero padded)
    Month - month name
    DD - day number (zero padded)

    Example: ('2020:01:22 18:00:00')

    /2020/01 - January/22

    :param datetime_string: string
    :return: string
    """

    path = ""

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
                path = os.path.join(year, month, day)

    return path


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


def sort_hierarchical_by_date(source_path, destination_path):
    """
    Iterate through the files, in the provided path, and sort them into a hierarchical folder structure, in the
    following format:

    destination_path/YYYY/MM - Month/DD

    YYYY - four digit year
    MM - month number (zero padded)
    Month - month name
    DD - day number (zero padded)

    Example: (January 22, 2020)

    /destination_path/2020/01 - January/22

    :param source_path:
    :param destination_path:
    :return:
    """


if __name__ == '__main__':

    source_path = ""
    destination_path = ""

    sorting_scheme = sort_hierarchical_by_date
    sort_files(source_path, destination_path, sorting_scheme)
