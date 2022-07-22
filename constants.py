API_KEY = "privet"


# group_id = "-1001645411567"
# channel_id = "-1001589660583"

chat_id_dic = {"Group": "@robotons_chat", "Channel": "@robotons"}

group_id = "@robotons_chat"
channel_id = "@robotons"

defaults_messages = {
    "start": """🇷🇺 🇷🇺
Привет. 🤖 
Чтобы принять участие в NFT Airdrop,
пожалуйста, подпишитесь на наш <a href='https://t.me/robotons'>канал</a> и <a href='https://t.me/robotons_chat'>группу</a>
Затем отправьте /verify для подтверждения подписки.

🇬🇧 🇬🇧
Hello. 🤖
To participate in NFT Airdrop,
please subscribe to our <a href='https://t.me/robotons'>Channel</a> and <a href='https://t.me/robotons_chat'>Group</a>.
Then send /verify to verify your subscription ."""
,
    "verify_error": """🇷🇺 🇷🇺
Не удалось выполнить проверку.
Пожалуйста, подпишитесь на наш <a href='https://t.me/robotons'>канал</a> и <a href='https://t.me/robotons_chat'>группу</a>.
Затем отправьте /verify, чтобы еще раз подтвердить подписку.

🇬🇧 🇬🇧
Verification failed.
Please subscribe to our <a href='https://t.me/robotons'>Channel</a> and <a href='https://t.me/robotons_chat'>Group</a>.
Then send /verify to verify your subscription  again."""
,
    "verified_msg": """🇷🇺 🇷🇺
Проверено успешно.🥳
Пожалуйста, пришлите адрес вашего кошелька.

🇬🇧 🇬🇧
Verified successfully.🥳
Please send your wallet address.

""",
    "wallet_added": """🇷🇺 🇷🇺
Поздравляем.🎉
Надеюсь, вы выиграете NFT.🎁😇

🇬🇧 🇬🇧
Congratulations.🎉
I hope you win a NFT.🎁😇
""",
    "wallet_exist": """🇷🇺 🇷🇺
Кошелек уже добавлен.
Надеюсь, вы выиграете NFT.🎁😇

🇬🇧 🇬🇧
Wallet already added.
I hope you win a NFT.🎁😇""",
}
