

### 必要な環境変数

#### Djangoの環境変数

- `DEBUG` : Falseにしてください
- `HOST_NAME` : ドメイン名を入れてください
- `DB_NAME` : HerokuPostgres の DBの名前
- `DB_USER` : HerokuPostgres の ユーザー名
- `DB_PASS` : HerokuPostgres の ユーザーのパスワード
- `DB_HOST` : HerokuPostgres の ホスト名

- `SECRET_KEY` : https://noauto-nolife.com/post/django-secret-key-regenerate/ に書かれてあるソースコードをもとにシークレットキーを再発行してください

#### Stripeの環境変数

- `STRIPE_API_KEY` : Stripeの秘密鍵
- `STRIPE_PUBLISHABLE_KEY` : Stripeの公開鍵
- `STRIPE_PRICE_ID` : Stripeのサブスク商品のID

#### Cloudinaryの環境変数

- `CLOUD_NAME` : Cloudinaryの名前
- `API_KEY` : CloudinaryのAPI_KEY
- `API_SECRET` : CloudinaryのAPI_SECRET

https://noauto-nolife.com/post/django-deploy-heroku-cloudinary/



### Stripeサブスク商品の作り方

https://dashboard.stripe.com/test/products

にて、『+ 商品を追加』をクリックして商品を作る。
作った商品のAPI IDを `STRIPE_PRICE_ID`に当てる。


