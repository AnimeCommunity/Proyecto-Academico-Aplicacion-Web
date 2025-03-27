from django import forms
from.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion", "categoria", "disponible", "imagen"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-input", "placeholder": "Nombre del producto", "required": True}),
            "precio": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Precio", "required": True}),
            "descripcion": forms.Textarea(attrs={"class": "form-textarea", "rows": 3, "placeholder": "Descripción", "required": True}),
            "categoria": forms.TextInput(attrs={"class": "form-input", "placeholder": "Categoría", "required": True}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-checkbox", "required": True}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-file"}),
        }