from django.views.generic import DetailView
from django.db import connection
from . import models


class LoanDetailsView(DetailView):
    template_name = 'loan_details.html'

    def get_object(self, queryset=None):
        """
        получить из обьектов модели кредитной заявки (!!!) уникальные id производителей всех
            товаров, которые связаны с этим контрактом
        """
        pk = self.kwargs['pk']
        producers = []

        # обращение через модель Кредитной заявки. Снижаем количество запросов к БД
        qs = models.LoanApplication.objects.select_related('contract').get(contract_id=pk).contract.products.all()
        print(connection.queries)

        # получаем производителей
        for product in qs:
            producers.append(product.producer.id)

        # отдаем только уникальные (?)
        return set(producers)
