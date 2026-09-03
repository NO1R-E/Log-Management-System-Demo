from .aws_norm import normalize_aws
from .ad_norm import normalize_ad
from .api_norm import normalize_api
from .m365_norm import normalize_m365

NORMALIZERS = {
    "aws": normalize_aws,
    "ad": normalize_ad,
    "api": normalize_api,
    "m365": normalize_m365,
}