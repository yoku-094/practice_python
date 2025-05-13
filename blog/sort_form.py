from django import forms

class SortForm(forms.Form):
    SORT_CHOICES = [
        ('-created_date', '新しい順'),
        ('created_date', '古い順'),
        ('title', 'タイトル昇順'),
        ('-title', 'タイトル降順'),
    ]
    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'onchange': 'this.form.submit();',
            'class': 'form-control',
        })
    )
