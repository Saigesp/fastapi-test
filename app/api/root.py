async def get_root():
    return {
        "endpoints": [
            "/v1/postal_codes/",
            "/v1/paystats/age-gender/{postal_code_id}",
            "/v1/paystats/times-series/{postal_code_id}",
        ]
    }
