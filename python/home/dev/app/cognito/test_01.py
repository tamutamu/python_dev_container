import boto3
from pprint import pprint

client = boto3.client('cognito-idp')

user_pool_id = 'ap-northeast-1_xLaQkKqpe'
app_client_id = '3o72755fpad723ot6j859s848u'


def sign_up(user_name, password, user_attrs):
    """
    ユーザ登録
    """
    try:
        res = client.sign_up(
            ClientId=app_client_id,
            Username=user_name,
            Password=password,
            UserAttributes=user_attrs)

        pprint(res)

    except Exception as e:
        pprint(e)


def sign_up_confirm(user_name, code):
    """
    ユーザ登録確認
    """
    try:
        res = client.confirm_sign_up(
            ClientId=app_client_id,
            Username=user_name,
            ConfirmationCode=code,
        )

        pprint(res)

    except Exception as e:
        pprint(e)


def resend_confirm_code(user_name):
    """
    ユーザ登録確認コード再送信
    """
    try:
        res = client.resend_confirmation_code(
            ClientId=app_client_id,
            Username=user_name,
        )

        pprint(res)

    except Exception as e:
        pprint(e)


def sign_in(user_name, password, user_attrs):
    """
    ユーザログイン
    """
    try:
        res = client.sign(
            ClientId=app_client_id,
            Username=user_name,
            Password=password,
            UserAttributes=user_attrs)

        pprint(res)

    except Exception as e:
        pprint(e)


###############################
### Main ###
###############################
user_attrs = [{'Name': 'email', 'Value': 'tamutamu.dev@gmail.com'},
              {'Name': 'birthdate', 'Value': '1999/01/01'}]

# sign_up('tamura', '1029384534928', user_attrs)

# resend_confirm_code('tamura')

confirm_code = input('Input confirm code')
sign_up_confirm('tamura', confirm_code)
