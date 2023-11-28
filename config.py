# -*- coding: utf-8 -*-

# (c) @maybeslow (Github) | https://t.me/birsamil | @birsamil (Telegram)

# ==============================================================================
#
# Project: EtiketTaggerBot
# Copyright (C) 2021-2022 by maybeslow@Github, < https://github.com/maybeslow >.
#
# This file is part of < https://github.com/maybeslow/Tagger > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see <https://github.com/maybeslow >
#
# All rights reserved.
#
# ==============================================================================
#
# Proje: EtiketTaggerBot
# Telif Hakkı (C) 2021-2022 maybeslow@Github, <https://github.com/maybeslow>.
#
# Bu dosya <https://github.com/maybeslow/Tagger> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. <https://github.com/maybeslow/Tagger >
#
# Her hakkı saklıdır.
#
# ========================================================================




import os
import heroku3
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient, events
import random

#
# 
api_id = 25114508 #my.telegram.org/apps adresinden alabilirsiniz 
api_hash = "993ccdfe81548dade420e81bcd6807ce" #my.telegram.org/apps adresinden alabilirsiniz
bot_token = "6645400469:AAEHTsNLDuwbd9AAmScXJrq3NzWna-9aE-c" #botfatherdan alabilirsiniz

client = TelegramClient("Samil", api_id, api_hash).start(bot_token=bot_token)

USERNAME = "ahriV2_bot" #botunuzun kullanıcı adı
log_qrup = -1001910817002 #log qrupunuzun idsi
startmesaj = "💌 Bazı Kullanışlı Özelliklere Sahip Telegram Üye Etiketleme Botuyum\n📚 Komutlar Butonuna Tıklayın Ve Komutları Öğrenin..." #start mesajınız
komutlar = "🇹🇷 𝖳𝗎𝗆 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋 ;\n\n» /utag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 5'𝗅𝗂 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /tag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝗍𝖾𝗄 𝗍𝖾𝗄 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /atag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂𝗅𝖾𝗋𝗂 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /etag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝖾𝗆𝗈𝗃𝗂𝗅𝖾𝗋𝗅𝖾 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /stag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝗀𝗎𝗓𝖾𝗅 𝗌𝗈𝗓𝗅𝖾𝗋𝗅𝖾 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /cancel =>\n   - 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗋 ." #komutların olduğu mesaj
qrupstart = "• 𝖲𝗎𝖺𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗄𝗍𝖺𝗒𝗂𝗆 . . .\n\n• 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 𝖡𝗈𝗍𝗎𝗇 𝗂𝖼𝖾𝗋𝗂𝗌𝗂𝗇𝖾 𝗀𝗂𝗋𝗂𝗉 𝖻𝖺𝗌𝗅𝖺𝗍𝗂𝗇 . . ." #aktif olduğunda gruba gelen mesaj
support = "redhackchet" #destek qrupunuzun kullanıcı adı
sahib = "rahmetiNC" #sahibinizin kullanıcı adı
noadmin = "➻ Üzgünüm Ama Yönetici Değilsiniz ." #yönetici olmayanlar için mesaj

#
# 
# 
# 

