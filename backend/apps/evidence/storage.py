from storages.backends.s3 import S3Storage


class PrivateEvidenceStorage(S3Storage):
    default_acl = "private"
    querystring_auth = True
    file_overwrite = False
    custom_domain = None
