                                    png_sticker=open('kangsticker.png', 'rb'), emojis=sticker_emoji)
            msg.reply_text(f"Sticker successfully added to [pack](t.me/addstickers/{packname})" +
                            f"\nEmoji is: {sticker_emoji}", parse_mode=ParseMode.MARKDOWN)
        except OSError as e:
            msg.reply_text("I can only kang images m8.")
            print(e)
            return
        except TelegramError as e:
            if (
                e.message
                == "Internal Server Error: sticker set not found (500)"
            ):
                msg.reply_text("Sticker successfully added to [pack](t.me/addstickers/%s)" % packname + "\n"
                            "Emoji is:" + " " + sticker_emoji, parse_mode=ParseMode.MARKDOWN)
            elif e.message == "Invalid sticker emojis":
                msg.reply_text("Invalid emoji(s).")
            elif e.message == "Sticker_png_dimensions":
                im.save(kangsticker, "PNG")
                bot.add_sticker_to_set(user_id=user.id, name=packname,
                                        png_sticker=open('kangsticker.png', 'rb'), emojis=sticker_emoji)
                msg.reply_text("Sticker successfully added to [pack](t.me/addstickers/%s)" % packname + "\n" +
                            "Emoji is:" + " " + sticker_emoji, parse_mode=ParseMode.MARKDOWN)
            elif e.message == "Stickers_too_much":
                msg.reply_text("Max packsize reached. Press F to pay respecc.")
            elif e.message == "Stickerset_invalid":
                makepack_internal(msg, user, open('kangsticker.png', 'rb'), sticker_emoji, bot, packname, packnum)
            print(e)
    else:
        packs = "Please reply to a sticker, or image to kang it!\nOh, by the way. here are your packs:\n"
        if packnum > 0:
            firstpackname = "a" + str(user.id) + "_by_"+bot.username
            for i in range(packnum + 1):
                if i == 0:
                    packs += f"[pack](t.me/addstickers/{firstpackname})\n"
                else:
                    packs += f"[pack{i}](t.me/addstickers/{packname})\n"
        else:
            packs += f"[pack](t.me/addstickers/{packname})"
        msg.reply_text(packs, parse_mode=ParseMode.MARKDOWN)
    if os.path.isfile("kangsticker.png"):
        os.remove("kangsticker.png")


def makepack_internal(msg, user, png_sticker, emoji, bot, packname, packnum):
    name = user.first_name
    name = name[:50]
    try:
        extra_version = " " + str(packnum) if packnum > 0 else ""
        success = bot.create_new_sticker_set(user.id, packname, f"{name}s kang pack" + extra_version,
                                             png_sticker=png_sticker,
                                             emojis=emoji)
    except TelegramError as e:
        print(e)
        if (
            e.message
            == "Internal Server Error: created sticker set not found (500)"
        ):
            msg.reply_text("Sticker pack successfully created. Get it [here](t.me/addstickers/%s)" % packname,
                   parse_mode=ParseMode.MARKDOWN)
        elif e.message == "Peer_id_invalid":
            msg.reply_text("Contact me in PM first.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                text="Start", url=f"t.me/{bot.username}")]]))
        elif e.message == "Sticker set name is already occupied":
            msg.reply_text("Your pack can be found [here](t.me/addstickers/%s)" % packname,
                           parse_mode=ParseMode.MARKDOWN)
        return

    if success:
        msg.reply_text("Sticker pack successfully created. Get it [here](t.me/addstickers/%s)" % packname,
                       parse_mode=ParseMode.MARKDOWN)
    else:
        msg.reply_text("Failed to create sticker pack. Possibly due to blek mejik.")


kang_handler = CommandHandler('kang', kang, pass_args=True)
kangurl_handler = CommandHandler('kangurl', kangurl, pass_args=True)
start_handler = CommandHandler('start', start)

dispatcher.add_handler(kang_handler)
dispatcher.add_handler(kangurl_handler)
dispatcher.add_handler(start_handler)

updater.start_polling(timeout=15, read_latency=4)
updater.idle()
