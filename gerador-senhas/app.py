from ttkbootstrap import *

root = Window(themename="darkly")


chk_btn = Checkbutton(root, text="Incluir Caracteres Númericos (0-9)")
chk_btn.pack(side=LEFT, padx=5, pady=10)

chk_btn = Checkbutton(root, text="Incluir Caracteres Especiais (!-*)")
chk_btn.pack(side=LEFT, padx=5, pady=10)

chk_btn = Checkbutton(root, text="Incluir Caracteres do Alfabeto (a-Z))")
chk_btn.pack(side=TOP, padx=5, pady=10)
chk_btn = Checkbutton(root, text="Incluir Caracteres Maiúsculos (a-z)", state=DISABLED)
chk_btn.pack(side=TOP, padx=5, pady=10)
chk_btn = Checkbutton(root, text="Incluir Caracteres Minúsculos (A-Z)", state=DISABLED)
chk_btn.pack(side=TOP, padx=5, pady=10)

btn = Button(root, text="Gerar Senha", bootstyle=(INFO, OUTLINE))
btn.pack(side=BOTTOM, padx=5, pady=10)

root.mainloop()
