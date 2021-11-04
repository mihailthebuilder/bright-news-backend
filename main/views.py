from .sentiment import sentiment_analyze
from .standardize import sen_stand
from .models import WebsiteModel, FailedWebsiteModel
from rest_framework import views
from rest_framework.response import Response

# Create your views here.


class CalculateView(views.APIView):
    def post(self, request):
        url = request.data.get("url")
        results = sentiment_analyze(url)

        context = {
            "success": results["success"],
            "url": url,
        }

        if results["success"]:

            website = WebsiteModel(
                url=results["url_analyzed"],
                score=results["score"],
                raw_data=results["raw_data"],
            )
            website.save()

            website_stand_li = sen_stand(
                website_model_list=WebsiteModel.objects.all(),
                range_min=0,
                range_max=100,
            )

            context.update(
                [
                    ("website_raw_data", results["raw_data"]),
                    ("website_li", website_stand_li),
                    ("url_analyzed", results["url_analyzed"]),
                ]
            )
        else:
            website = FailedWebsiteModel(url=url, error_message=results["message"])
            context["message"] = results["message"]
            website.save()

        return Response(context)
