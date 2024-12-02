from unittest.mock import Mock, patch

import pytest
from sqlalchemy.orm import Session

from app.models import Guild
from app.repositories import GuildRepository
from app.schemas import GuildCreate
from app.services import GuildService


@pytest.fixture
def mock_session():
    return Mock(spec=Session)


@pytest.fixture
def service(mock_session):
    return GuildService(mock_session)


@pytest.mark.asyncio
@patch.object(GuildRepository, "get_guild")
async def test_get_guild_exists(mock_get_guild, service):
    guild_id = 1
    guild = Guild(id=guild_id)

    mock_get_guild.return_value = guild

    assert await service.get_guild(guild_id) == guild


@pytest.mark.asyncio
@patch.object(GuildRepository, "get_guild")
async def test_get_guild_not_exists(mock_get_guild, service):
    guild_id = 1

    mock_get_guild.return_value = None

    with pytest.raises(Exception):
        await service.get_guild(guild_id)


@pytest.mark.asyncio
@patch.object(GuildRepository, "create_guild")
@patch.object(GuildRepository, "get_guild")
async def test_create_guild_success(mock_get_guild, mock_create_guild, service):
    guild_id = 1
    guild = Guild(id=guild_id)

    mock_get_guild.return_value = None
    mock_create_guild.return_value = guild

    data = GuildCreate(id=guild_id)
    assert await service.create_guild(data) == guild


@pytest.mark.asyncio
@patch.object(GuildRepository, "get_guild")
async def test_create_guild_failure(mock_get_guild, service):
    guild_id = 1
    guild = Guild(id=guild_id)

    mock_get_guild.return_value = guild

    with pytest.raises(Exception):
        await service.create_guild(guild_id)


@pytest.mark.asyncio
@patch.object(GuildRepository, "delete_guild")
@patch.object(GuildRepository, "get_guild")
async def test_delete_guild_success(mock_get_guild, mock_delete_guild, service):
    guild_id = 1
    guild = Guild(id=guild_id)

    mock_get_guild.return_value = guild
    mock_delete_guild.return_value = True

    assert await service.delete_guild(guild_id)


@pytest.mark.asyncio
@patch.object(GuildRepository, "get_guild")
async def test_delete_guild_failure(mock_get_guild, service):
    guild_id = 1

    mock_get_guild.return_value = None

    with pytest.raises(Exception):
        await service.delete_guild(guild_id)
