import unittest
from parameter_store import S3
from parameter_store import exceptions


class TestS3(unittest.TestCase):
    def test_bucket_found(self):
        try:
            S3("fdotest").get("whatever")
        except exceptions.NoSuchStoreException as e:
            bucket_found = False
        except exceptions.NoSuchKeyException as e:
            bucket_found = True
        else:
            bucket_found = True

        self.assertTrue(bucket_found)

    def test_bucket_not_found(self):
        try:
            S3("fakebucket123123vvajdfpggazz").get("whatever")
        except exceptions.NoSuchStoreException as e:
            bucket_failure_caught = True
        else:
            bucket_failure_caught = False

        self.assertTrue(bucket_failure_caught)

    def test_file_found(self):
        try:
            S3("fdotest").get("fixtures/parameter_store/fixture.txt")
        except Exception as e:
            file_found = False
        else:
            file_found = True

        self.assertTrue(file_found)

    def test_file_not_found(self):
        try:
            S3("fdotest").get("this_key_does_not_exist")
        except exceptions.NoSuchKeyException as e:
            file_failure_caught = True
        else:
            file_failure_caught = False

        self.assertTrue(file_failure_caught)

        """
        file_not_found = s3
        fake_failed =
        self.assertFalse(fake_failed)

        client.make_clock(
            "banana", start=datetime.now().astimezone(), interval_seconds=300
        )
        real_success = client.has_clock("banana")
        self.assertTrue(real_success)
        """
