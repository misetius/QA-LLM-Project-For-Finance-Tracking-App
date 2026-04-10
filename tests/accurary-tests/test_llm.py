import pytest
import json

class TestRegression:
    def test_return_products_in_the_receipt(self, model_client, clear_image_in_b64, report):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(clear_image_in_b64, question)
        try:
            assert "ed" in answer.lower()
            assert "skyr" in answer.lower()
            assert "purukumi" in answer.lower()
            assert "muovikassi" in answer.lower()
            report.true_positive()
        except AssertionError:
            report.false_negative()

    def test_categorize_products_in_the_receipt(self, model_client, clear_image_in_b64, report):
        question = """Categorize the products in the receipt that was sent with the prompt into these categories: Food, drinks, 
        Entertainment, Apartment, Electronics, Sports, Other. 
        Return the answer in a list where each item is in json {"product": "product name", "category": "category name", "price": "price"} format. 
        Response should only have this list of json data and nothing else. In the answer price should be in format 0.00. Ignore the KPL at the left of the receipt.
        Add deposit in the receipt to the price of the drinks. For example if there is a drink that costs 1.50 and deposit for that drink is 0.10, then the price in the answer should be 1.60.
        """
        
        answer = model_client.generate_answer(clear_image_in_b64, question)
        print(answer)
        answer = json.loads(answer)
        print(answer)
        sum = 0
        for i in answer:
            sum += float(i['price'].replace(",", "."))
        try:
            assert len(answer) == 9
            assert sum == 27.17
            report.true_positive()
        except AssertionError:
            report.false_negative()

class TestHallucination:
    def test_random_b64_string(self, model_client, random_b64_string, report):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(random_b64_string, question)
        try:
            assert "sorry" in answer.lower() or "cannot" in answer.lower() or "no image" in answer.lower() or "failed" in answer.lower() or "invalid" in answer.lower() or "understand" in answer.lower()
            report.true_negative()
        except AssertionError:
            report.false_positive()

    def test_non_receipt_image(self, model_client, random_image_in_b64, report):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(random_image_in_b64, question)
        try:
            assert "sorry" in answer.lower() or "cannot" in answer.lower() or "no image" in answer.lower() or "failed" in answer.lower() or "invalid" in answer.lower() or "understand" in answer.lower()
            report.true_negative()
        except AssertionError:
            report.false_positive()
        

class TestEdgeCases:
    def test_ripped_receipt(self, model_client, edge_case_image_in_b64_ripped_receipt, report):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(edge_case_image_in_b64_ripped_receipt, question)
        try:
            assert "monster" in answer.lower()
            assert "jenkki fresh apple crush" in answer.lower()
            report.true_positive()
        except AssertionError:
            report.false_negative()

    def test_receipt_from_side(self, model_client, edge_case_image_in_b64_image_from_side, report):
        question = "What products are in the image of receipt that was sent with the prompt?"
        answer = model_client.generate_answer(edge_case_image_in_b64_image_from_side, question)
        try:
            assert "monster" in answer.lower()
            assert "jenkki fresh apple crush" in answer.lower()
            report.true_positive()
        except AssertionError:
            report.false_negative()

    def test_categorize_products_in_the_receipt_from_side(self, model_client, edge_case_image_in_b64_image_from_side, report):
        question = """Categorize the products in the receipt that was sent with the prompt into these categories: Food, drinks, 
        Entertainment, Apartment, Electronics, Sports, Other. 
        Return the answer in a list where each item is in json {"product": "product name", "category": "category name", "price": "price"} format. 
        Response should only have this list of json data and nothing else. In the answer price should be in format 0.00. Ignore the KPL at the left of the receipt.
        Add deposit in the receipt to the price of the drinks. For example if there is a drink that costs 1.50 and deposit for that drink is 0.10, then the price in the answer should be 1.60.
        """
        
        answer = model_client.generate_answer(edge_case_image_in_b64_image_from_side, question)
        print(answer)
        answer = json.loads(answer)
        print(answer)
        sum = 0
        for i in answer:
            sum += float(i['price'].replace(",", "."))
        try:
            assert len(answer) == 2
            assert sum == 4.04
            report.true_positive()
        except AssertionError:
            report.false_negative()


    def test_categorize_products_in_the_ripped_receipt(self, model_client, edge_case_image_in_b64_ripped_receipt, report):
        question = """Categorize the products in the receipt that was sent with the prompt into these categories: Food, drinks, 
        Entertainment, Apartment, Electronics, Sports, Other. 
        Return the answer in a list where each item is in json {"product": "product name", "category": "category name", "price": "price"} format. 
        Response should only have this list of json data and nothing else. In the answer price should be in format 0.00. Ignore the KPL at the left of the receipt.
        Add deposit in the receipt to the price of the drinks. For example if there is a drink that costs 1.50 and deposit for that drink is 0.10, then the price in the answer should be 1.60.
        """
        
        answer = model_client.generate_answer(edge_case_image_in_b64_ripped_receipt, question)
        print(answer)
        answer = json.loads(answer)
        print(answer)
        sum = 0
        for i in answer:
            sum += float(i['price'].replace(",", "."))
        try:
            assert len(answer) == 2
            assert sum == 4.04
            report.true_positive()
        except AssertionError:
            report.false_negative()