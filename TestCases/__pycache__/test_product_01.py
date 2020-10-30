def test_products_display_correctly(self):
    products_page = ProductsPage(self.driver)
    products = TestData.getProducts()
    
    for index, expected_product in enumerate(products, start =1):
    "Add & Remove all Products"
        products_page.add_product_to_cart(index)
        self.assertTrue(products_page.dose_remove_button_exist(index))
        self.assertEqual(1, products_page.get_product_badge())
        
        products_page.remove_product_from_cart(index)
        self.asserTrue(products_page.does_add_button_exist(index))
        
        actual_product = products_page.get_product_info(index)
        assertion = Assertion()
        assertion.compare_products(actual_product, expected_product)

if __name__ == "__main__":
    unitest.main()