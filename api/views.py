from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnalyzeRequestSerializer
from .gemini import get_tone_and_intent
from .suggestions import suggest_actions
from .models import QueryLog

class AnalyzeView(APIView):
    def post(self, request):
        serializer = AnalyzeRequestSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data["query"]
            analysis = get_tone_and_intent(query)
            tone = analysis.get("tone", "Unknown")
            intent = analysis.get("intent", "Unknown")

            suggestions = suggest_actions(intent)

            log = QueryLog.objects.create(
                query=query,
                tone=tone,
                intent=intent,
                suggested_actions=suggestions
            )

            return Response({
                "query": query,
                "analysis": {
                    "tone": tone,
                    "intent": intent
                },
                "suggested_actions": suggestions
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)