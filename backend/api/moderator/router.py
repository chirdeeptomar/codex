from ninja import Router

router = Router(tags=["moderator"])


@router.get("/ping")
def ping(request):
    return {"status": "ok"}
