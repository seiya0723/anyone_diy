

## やること

### デザインのやること

DjangoMessageFrameworkの表示
レスポンシブ化のチェック


ユーザーのアイコン表示
画像のinputタグにサムネイルを表示させる形式に仕立てる


サマーノートのh1タグなどの装飾を個別にするか検討


プロジェクト一覧表示時に作業難度、所要時間をもう少し見やすくシンプルに表現する。


### システムのやること

Stripeによるサブスク処理
退会処理

検索処理をもう少し高度に(プロジェクトはカテゴリ検索を実装)

お気に入りに検索機能を







## やった


- プロジェクトの編集・削除処理
- マイページからプロジェクト・コミュニティの作成

- フィードバックの削除処理
- コミュニティの参加と閉鎖(削除)

- トピック投稿時、コミュニティ作成時に画像の投稿を許可
- トピックの削除機能
- トピックメッセージの削除機能

- Django-cleanupの実装


## 現状の問題

- コミュニティの参加処理とコミュニティ作成時のmembersフィールドのバリデーションが一貫性がなくておかしい(FIXMEの部分)
- プロジェクト編集時の素材削除処理のロジックが複雑なため、後回し。


