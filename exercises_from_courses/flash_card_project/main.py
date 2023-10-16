from src.buttons import FlashyButton
from src.card_operations import CardOperations


main = CardOperations()
button_ok = FlashyButton(
    button_img="flash_card_project\images\\right.png", button_col=1, button_row=1)
button_wrong = FlashyButton(
    button_img="flash_card_project\images\\wrong.png", button_col=0, button_row=1)

button_ok.config(command=main.next_card)
button_wrong.config(command=main.next_card)

main.window.mainloop()
