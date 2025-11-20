import json
import re
import logging
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Link
from .utils import generate_short_code, validate_url, validate_code


@require_http_methods(["GET", "OPTIONS"])
def healthz(request):
    response = JsonResponse({"ok": True, "version": "1.0"})
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def create_link(request):
    logger = logging.getLogger(__name__)
    try:
        data = json.loads(request.body)
        target_url = data.get('target_url')
        print(data)
        code = data.get('code')

        if not target_url:
            logger.error("No target URL provided")
            response = JsonResponse({"error": "Target URL is required"}, status=400)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response

        # Add https if missing and validate URL format
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
            if not re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', target_url):
                logger.error(f"Invalid URL format: {target_url}")
                response = JsonResponse({"error": "Invalid URL format"}, status=400)
                response['Access-Control-Allow-Origin'] = '*'
                response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
                response['Access-Control-Allow-Headers'] = 'Content-Type'
                return response

        if not validate_url(target_url):
            response = JsonResponse({"error": "Invalid URL"}, status=400)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response

        if code:
            if not validate_code(code):
                logger.error(f"Invalid code format: {code}")
                response = JsonResponse({"error": "Code must be 6-10 alphanumeric characters"}, status=400)
                response['Access-Control-Allow-Origin'] = '*'
                response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
                response['Access-Control-Allow-Headers'] = 'Content-Type'
                return response
            if Link.objects.filter(code=code).exists():
                logger.error(f"Code already exists: {code}")
                response = JsonResponse({"error": "Code already exists"}, status=409)
                response['Access-Control-Allow-Origin'] = '*'
                response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
                response['Access-Control-Allow-Headers'] = 'Content-Type'
                return response
        else:
            code = generate_short_code()
            while Link.objects.filter(code=code).exists():
                code = generate_short_code()

        link = Link.objects.create(code=code, target_url=target_url)
        logger.info(f"Created new link: {code} -> {target_url}")
        response = JsonResponse({
            "code": code,
            "target_url": target_url,
            "short_url": f"{request.build_absolute_uri('/')[:-1]}/{code}"
        }, status=201)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {str(e)}")
        response = JsonResponse({"error": "Invalid JSON format"}, status=400)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        response = JsonResponse({"error": "Internal server error"}, status=500)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response


@require_http_methods(["GET"])
def list_links(request):
    links = Link.objects.all().order_by('-created_at')
    data = [
        {
            "code": link.code,
            "target_url": link.target_url,
            "clicks": link.clicks,
            "last_clicked": link.last_clicked.isoformat() if link.last_clicked else None,
            "created_at": link.created_at.isoformat(),
            "short_url": f"{request.build_absolute_uri('/')[:-1]}/{link.code}"
        } for link in links
    ]
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def link_stats(request, code):
    try:
        link = Link.objects.get(code=code)
        return JsonResponse({
            "code": link.code,
            "target_url": link.target_url,
            "clicks": link.clicks,
            "last_clicked": link.last_clicked.isoformat() if link.last_clicked else None,
            "created_at": link.created_at.isoformat(),
            "short_url": f"{request.build_absolute_uri('/')[:-1]}/{link.code}"
        })
    except Link.DoesNotExist:
        return JsonResponse({"error": "Link not found"}, status=404)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_link(request, code):
    try:
        link = Link.objects.get(code=code)
        link.delete()
        return JsonResponse({"message": "Link deleted"})
    except Link.DoesNotExist:
        return JsonResponse({"error": "Link not found"}, status=404)


@require_http_methods(["GET"])
def redirect_view(request, code):
    try:
        link = Link.objects.get(code=code)
        link.clicks += 1
        link.last_clicked = timezone.now()
        link.save()
        return redirect(link.target_url)
    except Link.DoesNotExist:
        return JsonResponse({"error": "Link not found"}, status=404)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["GET",'POST'])
def links_view(request):
    if request.method == 'GET':
        return list_links(request)
    elif request.method == 'POST':
        return create_link(request)
    elif request.method == 'OPTIONS':
        response = JsonResponse({})
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    return JsonResponse({"error": "Method not allowed"}, status=405)

@require_http_methods(["GET",'DELETE'])
@csrf_exempt
def link_detail_view(request, code):
    if request.method == 'GET':
        return link_stats(request, code)
    elif request.method == 'DELETE':
        return delete_link(request, code)
    return JsonResponse({"error": "Method not allowed"}, status=405)
