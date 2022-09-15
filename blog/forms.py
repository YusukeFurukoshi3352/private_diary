from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    email = forms.EmailField(label='email')
    title = forms.CharField(label='title', max_length=30)
    message = forms.CharField(label='message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'