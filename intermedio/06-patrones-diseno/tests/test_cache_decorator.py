from lab_patterns.providers.external_provider import ExternalCatalogProvider


def test_cache_decorator_avoids_duplicate_calls() -> None:
    provider = ExternalCatalogProvider()

    first = provider.fetch_product("EXT-001")
    second = provider.fetch_product("EXT-001")

    assert first == second
    assert provider.call_count == 1


def test_cache_uses_different_key_for_different_arguments() -> None:
    provider = ExternalCatalogProvider()

    provider.fetch_product("EXT-001")
    provider.fetch_product("EXT-002")

    assert provider.call_count == 2
