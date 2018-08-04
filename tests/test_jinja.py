from prefab import jinja


def test_render():
    assert jinja.render(template='foo') == 'foo'
    assert jinja.render(
        template='{{ var }}',
        context={'var': 'foo'},
    ) == 'foo'
