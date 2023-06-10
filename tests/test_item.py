from src.item import Item

test_item_1 = Item('test_1', 999.99, 100)
test_item_2 = Item('test_2', 50, 3)


def test_calculate_total_price():

    assert test_item_1.calculate_total_price() == 99999
    assert test_item_2.calculate_total_price() == 150


def test_apply_discount():
    test_item_1.apply_discount()
    test_item_2.apply_discount()
    assert test_item_1.price == 999.99
    assert test_item_2.price == 50

    Item.pay_rate = 0.9

    test_item_1.apply_discount()
    test_item_2.apply_discount()
    
    assert test_item_1.price == 899.991
    assert test_item_2.price == 45


def test_name():
    assert test_item_1.name == 'test_1'
    assert test_item_2.name == 'test_2'

    test_item_1.name = 'new_1'
    test_item_2.name = 'new_test_name_2'

    assert test_item_1.name == 'new_1'
    assert test_item_2.name == 'test_2'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 7

    item1 = Item.all[5]
    assert item1.name == 'Мышка'
    assert item1.price == 50
    assert item1.quantity == 5
