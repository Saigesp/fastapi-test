async def get_root():
    return {
        "endpoints": [
            "/v1/postal_codes/?bounds={bounds}",
            "/v1/paystats/age-gender/{postal_code_id}",
            "/v1/paystats/time-gender/{postal_code_id}",
            "/v1/adm1/{postal_code_prefix}",
        ]
    }
