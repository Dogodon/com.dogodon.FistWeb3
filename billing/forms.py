from django import forms

class AvoirArticleForm(forms.Form):
    designation = forms.CharField(max_length=200, label="Désignation")
    quantite = forms.IntegerField(min_value=1, label="Quantité")
    prix_unitaire = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        min_value=0,
        label="Prix unitaire"
    )
    famille = forms.CharField(max_length=50, required=False, label="Famille")

class AvoirForm(forms.Form):
    motif = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Motif de l'avoir",
        required=True
    )
    logo = forms.ImageField(required=False, label="Logo (optionnel)")