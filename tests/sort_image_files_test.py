import os
import sort_image_files
import unittest



class TestComputeHierarchicalPath(unittest.TestCase):

    def test_datetime_string_well_formed(self):
        """
        In this test case, a well formed datetime string has been provided.

        We expect that this should be successfully parsed, and the corresponding path computed.

        :return:
        """

        datetime_string = '2020:01:15 18:00:41'
        expected_result = os.path.join('2020', '01 - January', '15')
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_year_too_short(self):
        """
        In this test case, a malformed datetime string has been provided, where the year portion of the date is
        invalid (it is two digits, instead of the required four).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '20:01:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_year_missing(self):
        """
        In this test case, a malformed datetime string has been provided, where the year portion of the date is
        invalid (it is empty).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = ':01:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_month_too_small(self):
        """
        In this test case, a malformed datetime string has been provided, where the month portion of the date is
        invalid (it is outside of the lower bounds).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:00:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_month_too_large(self):
        """
        In this test case, a malformed datetime string has been provided, where the month portion of the date is
        invalid (it is outside of the upper bounds).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:13:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_month_too_short(self):
        """
        In this test case, a malformed datetime string has been provided, where the month portion of the date is
        invalid (it has only one digit, rather than two).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:1:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_month_too_long(self):
        """
        In this test case, a malformed datetime string has been provided, where the month portion of the date is
        invalid (it has more than two digits).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:001:15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_month_missing(self):
        """
        In this test case, a malformed datetime string has been provided, where the month portion of the date is
        invalid (it is empty).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020::15 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_day_too_small(self):
        """
        In this test case, a malformed datetime string has been provided, where the day portion of the date is
        invalid (it is outside of the lower bounds).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:01:00 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_day_too_large(self):
        """
        In this test case, a malformed datetime string has been provided, where the day portion of the date is
        invalid (it is outside of the upper bounds).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:01:32 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_day_too_short(self):
        """
        In this test case, a malformed datetime string has been provided, where the day portion of the date is
        invalid (it has only one digit, rather than two).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:01:1 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_day_too_long(self):
        """
        In this test case, a malformed datetime string has been provided, where the day portion of the date is
        invalid (it has more than two digits).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:01:015 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_malformed_day_missing(self):
        """
        In this test case, a malformed datetime string has been provided, where the day portion of the date is
        invalid (it is empty).

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '2020:01: 18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_missing_time(self):
        """
        In this test case, the time portion has been excluded, and only the date components are present. This should
        not present a problem, as it's only the date components that we're concerned with.

        We expect that this should be successfully parsed, and the corresponding path computed.

        :return:
        """

        datetime_string = '2020:01:15'
        expected_result = os.path.join('2020', '01 - January', '15')
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_missing_date(self):
        """
        In this test case, the date portion has been excluded, and only the time components are present. This is in
        a similar format to the date, as it is still three components which are separated by colons. But clearly this
        is not a proper date.

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = '18:00:41'
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)

    def test_datetime_string_empty(self):
        """
        In this test case, an empty datetime string is provided. Clearly this is not a proper date.

        We expect this to be caught, and for an empty string to be returned.

        :return:
        """

        datetime_string = ''
        expected_result = ''
        actual_result = sort_image_files.compute_hierarchical_path(datetime_string)

        self.assertEqual(actual_result, expected_result)


class TestIsYearValid(unittest.TestCase):

    def test_year_string_valid(self):
        """
        In this test case, a well formed, valid year has been provided.

        We expect that True should be returned.

        :return:
        """

        year = '2020'
        expected_result = True
        actual_result = sort_image_files.is_year_valid(year)

        self.assertEqual(actual_result, expected_result)

    def test_year_string_malformed_too_short(self):
        """
        In this test case, a malformed year has been provided. In this case, it is too short (two digits, instead of
        the required four).

        We expect that False should be returned.

        :return:
        """

        year = '20'
        expected_result = False
        actual_result = sort_image_files.is_year_valid(year)

        self.assertEqual(actual_result, expected_result)

    def test_year_string_malformed_too_long(self):
        """
        In this test case, a malformed year has been provided. In this case, it is too long (five digits, instead of
        the required four).

        We expect that False should be returned.

        :return:
        """

        year = '02020'
        expected_result = False
        actual_result = sort_image_files.is_year_valid(year)

        self.assertEqual(actual_result, expected_result)

    def test_year_string_malformed_not_numeric(self):
        """
        In this test case, a malformed year has been provided. In this case, it is the correct length, but is not a
        numeric value.

        We expect that False should be returned.

        :return:
        """

        year = 'aaaa'
        expected_result = False
        actual_result = sort_image_files.is_year_valid(year)

        self.assertEqual(actual_result, expected_result)

    def test_year_string_malformed_empty(self):
        """
        In this test case, a malformed year has been provided. In this case, it is an empty string.

        We expect that False should be returned.

        :return:
        """

        year = ''
        expected_result = False
        actual_result = sort_image_files.is_year_valid(year)

        self.assertEqual(actual_result, expected_result)


class TestIsMonthValid(unittest.TestCase):

    def test_month_string_valid(self):
        """
        In this test case, a well formed, valid month has been provided.

        We expect that True should be returned.

        :return:
        """

        month = '01'
        expected_result = True
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_too_small(self):
        """
        In this test case, a well formed month has been provided, but the value is invalid (it is outside of the
        lower bounds).

        We expect that False should be returned.

        :return:
        """

        month = '00'
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_too_large(self):
        """
        In this test case, a well formed month has been provided, but the value is invalid (it is outside of the
        upper bounds).

        We expect that False should be returned.

        :return:
        """

        month = '13'
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_too_short(self):
        """
        In this test case, a malformed month has been provided. In this case, it is too short (one digit, instead of
        the required two).

        We expect that False should be returned.

        :return:
        """

        month = '1'
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_too_long(self):
        """
        In this test case, a malformed month has been provided. In this case, it is too long (three digits, instead of
        the required two).

        We expect that False should be returned.

        :return:
        """

        month = '001'
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_not_numeric(self):
        """
        In this test case, a malformed month has been provided. In this case, it is the correct length, but is not a
        numeric value.

        We expect that False should be returned.

        :return:
        """

        month = 'aa'
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)

    def test_month_string_malformed_empty(self):
        """
        In this test case, a malformed month has been provided. In this case, it is an empty string.

        We expect that False should be returned.

        :return:
        """

        month = ''
        expected_result = False
        actual_result = sort_image_files.is_month_valid(month)

        self.assertEqual(actual_result, expected_result)


class TestIsDayValid(unittest.TestCase):

    def test_day_string_valid(self):
        """
        In this test case, a well formed, valid day has been provided.

        We expect that True should be returned.

        :return:
        """

        day = '01'
        expected_result = True
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_too_small(self):
        """
        In this test case, a well formed day has been provided, but the value is invalid (it is outside of the
        lower bounds).

        We expect that False should be returned.

        :return:
        """

        day = '00'
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_too_large(self):
        """
        In this test case, a well formed day has been provided, but the value is invalid (it is outside of the
        upper bounds).

        We expect that False should be returned.

        :return:
        """

        day = '32'
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_too_short(self):
        """
        In this test case, a malformed day has been provided. In this case, it is too short (one digit, instead of
        the required two).

        We expect that False should be returned.

        :return:
        """

        day = '1'
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_too_long(self):
        """
        In this test case, a malformed day has been provided. In this case, it is too long (three digits, instead of
        the required two).

        We expect that False should be returned.

        :return:
        """

        day = '001'
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_not_numeric(self):
        """
        In this test case, a malformed day has been provided. In this case, it is the correct length, but is not a
        numeric value.

        We expect that False should be returned.

        :return:
        """

        day = 'aa'
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)

    def test_day_string_malformed_empty(self):
        """
        In this test case, a malformed day has been provided. In this case, it is an empty string.

        We expect that False should be returned.

        :return:
        """

        day = ''
        expected_result = False
        actual_result = sort_image_files.is_day_valid(day)

        self.assertEqual(actual_result, expected_result)


class TestGetCreationDateFromFile(unittest.TestCase):

    def setUp(self):
        self.test_data_path = os.path.join(os.getcwd(), 'test_data')

    def test_valid_file_img_0766(self):
        """
        In this test case, a valid JPEG file, containing a creation date within the EXIF metadata is provided.

        We expect a date to be extracted.

        :return:
        """

        test_filename = 'IMG_0766.JPG'
        file_path = os.path.join(self.test_data_path, test_filename)
        expected_result = '2020:01:15 18:00:41'
        actual_result = sort_image_files.get_creation_date_from_file(file_path)

        self.assertEqual(actual_result, expected_result)

    def test_valid_file_img_0839_no_metadata(self):
        """
        In this test case, a valid JPEG file, containing no EXIF metadata is provided.

        We expect that an empty string will be returned, as there is no date to extract.

        :return:
        """

        test_filename = 'IMG_0839_no_metadata.JPG'
        file_path = os.path.join(self.test_data_path, test_filename)
        expected_result = ''
        actual_result = sort_image_files.get_creation_date_from_file(file_path)

        self.assertEqual(actual_result, expected_result)

    def test_invalid_file_img_0000_invalid(self):
        """
        In this test case, an invalid JPEG file is provided.

        We expect that an empty string will be returned, as there is no date to extract.

        :return:
        """

        test_filename = 'IMG_0000_invalid.JPG'
        file_path = os.path.join(self.test_data_path, test_filename)
        expected_result = ''
        actual_result = sort_image_files.get_creation_date_from_file(file_path)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()