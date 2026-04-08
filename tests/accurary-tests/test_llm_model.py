import pytest
import json

class TestRegression:
    def test_return_products_in_the_receipt(self, model_client, clear_image_in_b64):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(clear_image_in_b64, question)
        assert "ed" in answer.lower()
        assert "skyr" in answer.lower()
        assert "purukumi" in answer.lower()
        assert "muovikassi" in answer.lower()

    def test_categorize_products_in_the_receipt(self, model_client, clear_image_in_b64):
        question = """Categorize the products in the receipt that was sent with the prompt into these categories: Food, drinks, 
        Entertainment, Apartment, Electronics, Sports, Other. 
        Return the answer in a list where each item is in json {"product": "product name", "category": "category name", "price": "price"} format. Response should only have this list of json data and nothing else.
        If there is more than one product in the same category, they should be separate items in the list. KPL means quantity, so if there are 2 of the same product, they should be separate items in the list. product 
        names are on the left side and if there multiple of the same product, the quantity is under it with KPL.
        """
        
        answer = model_client.generate_answer(clear_image_in_b64, question)
        answer = json.loads(answer)
        print(answer)
        
        assert len(answer) == 15



#class TestHallucination:


#class TestEdgeCases:
    