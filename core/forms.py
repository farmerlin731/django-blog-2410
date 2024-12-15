from django import forms


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(required=True, label="你確定要刪除嗎？")
