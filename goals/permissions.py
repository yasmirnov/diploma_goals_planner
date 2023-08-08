from typing import Any

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView

from goals.models import GoalCategory, Goal, GoalComment, Board, BoardParticipant


class BoardPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Board) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'boards': obj}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner
        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCategoryPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalCategory) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'boards': obj.board}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]
        return BoardParticipant.objects.filter(**_filters).exists()


class GoalPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Goal) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'boards': obj.category.board}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]
        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCommentPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalComment) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user
