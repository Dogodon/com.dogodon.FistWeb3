from rest_framework import serializers
from .models import Invoice, Article, Customer

class GenderChoiceFieldSerializer(serializers.Field):
    """
    Champ personnalisé pour la gestion des choix de sexe.
    """

    def to_representation(self, obj):
        # Renvoie le label associé à la valeur de 'sex' (M ou F)
        return dict(SEX_TYPES).get(obj)

    def to_internal_value(self, data):
        # Ici, on accepte une chaîne de caractère correspondant à la valeur ('M' ou 'F')
        if data not in dict(SEX_TYPES).keys():
            raise serializers.ValidationError("Invalid gender value")
        return data


class CustomerTypeChoiceFieldSerializer(serializers.Field):
    """
    Champ personnalisé pour la gestion des choix des types de client.
    """

    def to_representation(self, obj):
        # Renvoie le label associé à la valeur de 'sex' (M ou F)
        return dict(CUSTOMER_TYPE_CHOICES).get(obj)

    def to_internal_value(self, data):
        # Ici, on accepte une chaîne de caractère correspondant à la valeur ('M' ou 'F')
        if data not in dict(CUSTOMER_TYPE_CHOICES).keys():
            raise serializers.ValidationError("Invalid CUSTOMER_TYPE_CHOICE value")
        return data


class ZoneTypeChoiceFieldSerializer(serializers.Field):
    """
    Champ personnalisé pour la gestion des choix des types de client.
    """

    def to_representation(self, obj):
        # Renvoie le label associé à la valeur de 'sex' (M ou F)
        return dict(ZONE_TYPE_CHOICES).get(obj)

    def to_internal_value(self, data):
        # Ici, on accepte une chaîne de caractère correspondant à la valeur ('M' ou 'F')
        if data not in dict(ZONE_TYPE_CHOICES).keys():
            raise serializers.ValidationError("Invalid ZONE_TYPE_CHOICE value")
        return data

class CustomerSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='save_by.get_full_name', read_only=True)

    created_date = serializers.SerializerMethodField()
    sex = GenderChoiceFieldSerializer()  # Utilisation du champ personnalisé pour 'sex'
    zone = ZoneTypeChoiceFieldSerializer()  # Utilisation du champ personnalisé pour 'zone'
    customer_type = CustomerTypeChoiceFieldSerializer()  # Utilisation du champ personnalisé pour 'customer_type'


    class Meta:
        model = Customer
        fields = [
            'id',
            'nom',
            'prenom',
            'email',
            'sex',
            'ville',
            'pays',
            'zone',
            'created_date',
            'customer_type',
            'creator_name',  # Ajouter le champ du créateur
            'telephone'
        ]

    def get_created_date(self, obj):
        return obj.created_date.strftime('%Y-4m-4d %H:%M:%S')
    



class ArticleSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'designation', 'quantity', 'unite', 'unit_price',
            'remise', 'tva', 'montant_ht', 'famille', 'total'
        ]

    def get_total(self, obj):
        return float(obj.get_total)

from billing.models import SEX_TYPES,CUSTOMER_TYPE_CHOICES,ZONE_TYPE_CHOICES








class InvoiceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    articles = ArticleSerializer(source='article_set', many=True)
    total = serializers.SerializerMethodField()
    invoice_type = serializers.CharField(source='get_invoice_type_display')

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_type', 'invoice_date_time', 'paid',
            'comments', 'total', 'customer', 'articles'
        ]

    def get_total(self, obj):
        return float(obj.get_total)
