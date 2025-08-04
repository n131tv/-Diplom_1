from praktikum.bun import Bun


class TestBun:

    """ Тест на получение наименования """
    def test_bun_name_is_expected(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    """ Тест на получение прайса """
    def test_bun_price_is_expected(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_price() == 988