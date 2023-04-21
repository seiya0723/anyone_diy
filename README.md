

### 必要な環境変数

- `DEBUG` : Falseにしてください
- `HOST_NAME` : ドメイン名を入れてください
- `DB_NAME` : HerokuPostgres の DBの名前
- `DB_USER` : HerokuPostgres の DBのユーザー
- `DB_PASS` : HerokuPostgres の DBのユーザーのパスワード
- `DB_HOST` : HerokuPostgres の DBの名前

- `SECRET_KEY` : https://noauto-nolife.com/post/django-secret-key-regenerate/ に書かれてあるソースコードをもとにシークレットキーを再発行してください

- `STRIPE_API_KEY` : Stripeの秘密鍵
- `STRIPE_PUBLISHABLE_KEY` : Stripeの公開鍵
- `STRIPE_PRICE_ID` : StripeのサブスクID


### Stripeサブスク商品の作り方

https://dashboard.stripe.com/test/products

にて、『+ 商品を追加』をクリックして商品を作る。
作った商品のAPI IDを `STRIPE_PRICE_ID`に当てる。


