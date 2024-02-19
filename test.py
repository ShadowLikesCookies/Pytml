from PytmlCompiler import main

if __name__ == "__main__":
    main(
        ("div", "login-container", [
            ("h1", "Login", "login-title"),
            ("form", "", "", {'action': 'login-form', 'method': 'post', 'children': [
                ("div", "form-group", [
                    ("label", "Username:", "username-label", {'for': 'username-input'}),
                    ("input", "", "username-input", {'type': 'text', 'id': 'username-input', 'placeholder': 'Enter your username'})
                ]),
                ("div", "form-group", [
                    ("label", "Password:", "password-label", {'for': 'password-input'}),
                    ("input", "", "password-input", {'type': 'password', 'id': 'password-input', 'placeholder': 'Enter your password'})
                ]),
                ("div", "form-group", [
                    ("button", "Login", "login-button")
                ])
            ]})
        ])
    )
