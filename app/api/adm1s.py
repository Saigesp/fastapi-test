from app.services.validation import validate_postal_code_prefix
from app.selectors.adm1s import get_adm1s_from_prefix
from app.serializers.adm1s import Adm1OutputSerializer


async def get_adm1_by_postal_code_prefix(prefix: str):
    validate_postal_code_prefix(prefix)
    data = await get_adm1s_from_prefix(prefix)

    return {
        "postal_code_prefix": prefix,
        "results": Adm1OutputSerializer(data).data,
    }
