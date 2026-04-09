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
        Return the answer in a list where each item is in json {"product": "product name", "category": "category name", "price": "price"} format. 
        Response should only have this list of json data and nothing else. In the answer price should be in format 0.00. Ignore the KPL at the left of the receipt.
        """
        
        answer = model_client.generate_answer(clear_image_in_b64, question)
        print(answer)
        answer = json.loads(answer)
        print(answer)
        sum = 0
        for i in answer:
            sum += float(i['price'].replace(",", "."))
        assert len(answer) == 11
        assert sum == 27.17

class TestHallucination:
    def test_random_b64_string(self, model_client):
        question = "What products are in the image of receipt that was sent with the prompt?"
        random_b64 = "VGhpcyBpcyBhIHJhbmRvbSBiNjQgc3RyaW5nIHRoYXQgZG9lc24ndCBjb250YWluIGFueSBpbWFnZSBkYXRhLg=="
        answer = model_client.generate_answer(random_b64, question)
        assert "sorry" in answer.lower() or "cannot" in answer.lower() or "no image" in answer.lower() or "failed" in answer.lower() or "invalid" in answer.lower() or "understand" in answer.lower()

    def test_non_receipt_image(self, model_client, random_image_in_b64):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(random_image_in_b64, question)
        assert "sorry" in answer.lower() or "cannot" in answer.lower() or "no image" in answer.lower() or "failed" in answer.lower() or "invalid" in answer.lower() or "understand" in answer.lower()

#class TestEdgeCases:
    