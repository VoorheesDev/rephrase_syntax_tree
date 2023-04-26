from apps.rephrase.utils import convert_ptree_to_str, generate_rephrased_ptrees, make_ptree
from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateRephrasedTreesAPIView(APIView):
    """View for creating new unique syntactic trees."""

    def post(self, request, *args, **kwargs):
        tree = request.query_params.get("tree")
        limit = request.query_params.get("limit")

        # validation
        if not tree:
            raise ValidationError("Missing required query parameter `tree`")
        if not limit:
            limit = settings.REPHRASE_LIMIT
        else:
            try:
                limit = int(limit)
            except ValueError:
                raise ValidationError("`limit` parameter must be integer")

        ptree = make_ptree(tree)
        rephrased_ptrees = [
            {"tree": convert_ptree_to_str(t)} for t in generate_rephrased_ptrees(ptree, limit)
        ]
        data = {"paraphrases": rephrased_ptrees}

        return Response(data, status=status.HTTP_201_CREATED)
