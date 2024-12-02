from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from sqlalchemy.orm import Session

from app.models import Guild, Message
from app.repositories import GuildRepository, MessageRepository
from app.schemas import MessageCreate
from app.services import LLMService, MessageService


@pytest.fixture
def mock_session():
    return Mock(spec=Session)


@pytest.fixture
def service(mock_session):
    return MessageService(mock_session)


@pytest.mark.asyncio
@patch.object(MessageRepository, "get_message")
async def test_get_message_exists(mock_get_message, service):
    message_id = 1
    guild_id = 1
    content = "a"
    timestamp = datetime(2000, 1, 1)
    message = Message(
        id=message_id,
        guild_id=guild_id,
        content=content,
        embedding=None,
        timestamp=timestamp,
    )

    mock_get_message.return_value = message

    assert await service.get_message(message_id) == message


@pytest.mark.asyncio
@patch.object(MessageRepository, "get_message")
async def test_get_message_not_exists(mock_get_message, service):
    message_id = 1

    mock_get_message.return_value = None

    with pytest.raises(Exception):
        await service.get_message(message_id)


@pytest.mark.asyncio
@patch.object(MessageRepository, "create_message")
@patch.object(LLMService, "embed_text")
@patch.object(MessageRepository, "get_message")
@patch.object(GuildRepository, "get_guild")
async def test_create_message_success(
    mock_get_guild, mock_get_message, mock_embed_text, mock_create_message, service
):
    guild_id = 1
    guild = Guild(id=guild_id)

    message_id = 1
    content = "a"
    embedding = None
    timestamp = datetime(2000, 1, 1)
    message = Message(
        id=message_id,
        guild_id=guild_id,
        content=content,
        embedding=embedding,
        timestamp=timestamp,
    )

    mock_get_guild.return_value = guild
    mock_get_message.return_value = None
    mock_embed_text.return_value = embedding
    mock_create_message.return_value = message

    data = MessageCreate(id=message_id, guild_id=guild_id, content=content, timestamp=timestamp)
    assert await service.create_message(data) == message


@pytest.mark.asyncio
@patch.object(GuildRepository, "get_guild")
async def test_create_message_failure_guild_not_exists(mock_get_guild, service):
    message_id = 1
    guild_id = 1
    content = "a"
    timestamp = datetime(2000, 1, 1)

    mock_get_guild.return_value = None

    data = MessageCreate(id=message_id, guild_id=guild_id, content=content, timestamp=timestamp)
    with pytest.raises(Exception):
        await service.create_message(data)


@pytest.mark.asyncio
@patch.object(MessageRepository, "get_message")
@patch.object(GuildRepository, "get_guild")
async def test_create_message_failure_message_exists(mock_get_guild, mock_get_message, service):
    guild_id = 1
    guild = Guild(id=guild_id)

    message_id = 1
    content = "a"
    timestamp = datetime(2000, 1, 1)
    message = Message(
        id=message_id,
        guild_id=guild_id,
        content=content,
        embedding=None,
        timestamp=timestamp,
    )

    mock_get_guild.return_value = guild
    mock_get_message.return_value = message

    data = MessageCreate(id=message_id, guild_id=guild_id, content=content, timestamp=timestamp)
    with pytest.raises(Exception):
        await service.create_message(data)


@pytest.mark.asyncio
@patch.object(MessageRepository, "delete_message")
@patch.object(MessageRepository, "get_message")
async def test_delete_guild_success(mock_get_message, mock_delete_message, service):
    message_id = 1
    guild_id = 1
    content = "a"
    timestamp = datetime(2000, 1, 1)
    message = Message(
        id=message_id,
        guild_id=guild_id,
        content=content,
        embedding=None,
        timestamp=timestamp,
    )

    mock_get_message.return_value = message
    mock_delete_message.return_value = True

    assert await service.delete_message(message_id)


@pytest.mark.asyncio
@patch.object(MessageRepository, "get_message")
async def test_delete_guild_failure(mock_get_message, service):
    message_id = 1

    mock_get_message.return_value = None

    with pytest.raises(Exception):
        await service.delete_message(message_id)
