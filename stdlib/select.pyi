import sys
from _typeshed import FileDescriptorLike
from collections.abc import Iterable
from types import TracebackType
from typing import Any
from typing_extensions import Self, final

if sys.platform != "win32":
    PIPE_BUF: int
    POLLERR: int
    POLLHUP: int
    POLLIN: int
    POLLMSG: int
    POLLNVAL: int
    POLLOUT: int
    POLLPRI: int
    POLLRDBAND: int
    if sys.platform == "linux":
        POLLRDHUP: int
    POLLRDNORM: int
    POLLWRBAND: int
    POLLWRNORM: int

class poll:
    def register(self, fd: FileDescriptorLike, eventmask: int = ...) -> None: ...
    def modify(self, fd: FileDescriptorLike, eventmask: int) -> None: ...
    def unregister(self, fd: FileDescriptorLike) -> None: ...
    def poll(self, timeout: float | None = ...) -> list[tuple[int, int]]: ...

def select(
    __rlist: Iterable[Any], __wlist: Iterable[Any], __xlist: Iterable[Any], __timeout: float | None = None
) -> tuple[list[Any], list[Any], list[Any]]: ...

error = OSError

if sys.platform != "linux" and sys.platform != "win32":
    # BSD only
    @final
    class kevent:
        data: Any
        fflags: int
        filter: int
        flags: int
        ident: int
        udata: Any
        def __init__(
            self,
            ident: FileDescriptorLike,
            filter: int = ...,
            flags: int = ...,
            fflags: int = ...,
            data: Any = ...,
            udata: Any = ...,
        ) -> None: ...
    # BSD only
    @final
    class kqueue:
        closed: bool
        def __init__(self) -> None: ...
        def close(self) -> None: ...
        def control(
            self, __changelist: Iterable[kevent] | None, __maxevents: int, __timeout: float | None = None
        ) -> list[kevent]: ...
        def fileno(self) -> int: ...
        @classmethod
        def fromfd(cls, __fd: FileDescriptorLike) -> kqueue: ...
    KQ_EV_ADD: int
    KQ_EV_CLEAR: int
    KQ_EV_DELETE: int
    KQ_EV_DISABLE: int
    KQ_EV_ENABLE: int
    KQ_EV_EOF: int
    KQ_EV_ERROR: int
    KQ_EV_FLAG1: int
    KQ_EV_ONESHOT: int
    KQ_EV_SYSFLAGS: int
    KQ_FILTER_AIO: int
    KQ_FILTER_NETDEV: int
    KQ_FILTER_PROC: int
    KQ_FILTER_READ: int
    KQ_FILTER_SIGNAL: int
    KQ_FILTER_TIMER: int
    KQ_FILTER_VNODE: int
    KQ_FILTER_WRITE: int
    KQ_NOTE_ATTRIB: int
    KQ_NOTE_CHILD: int
    KQ_NOTE_DELETE: int
    KQ_NOTE_EXEC: int
    KQ_NOTE_EXIT: int
    KQ_NOTE_EXTEND: int
    KQ_NOTE_FORK: int
    KQ_NOTE_LINK: int
    if sys.platform != "darwin":
        KQ_NOTE_LINKDOWN: int
        KQ_NOTE_LINKINV: int
        KQ_NOTE_LINKUP: int
    KQ_NOTE_LOWAT: int
    KQ_NOTE_PCTRLMASK: int
    KQ_NOTE_PDATAMASK: int
    KQ_NOTE_RENAME: int
    KQ_NOTE_REVOKE: int
    KQ_NOTE_TRACK: int
    KQ_NOTE_TRACKERR: int
    KQ_NOTE_WRITE: int

if sys.platform == "linux":
    @final
    class epoll:
        def __init__(self, sizehint: int = ..., flags: int = ...) -> None: ...
        def __enter__(self) -> Self: ...
        def __exit__(
            self,
            __exc_type: type[BaseException] | None = None,
            __exc_value: BaseException | None = ...,
            __exc_tb: TracebackType | None = None,
        ) -> None: ...
        def close(self) -> None: ...
        closed: bool
        def fileno(self) -> int: ...
        def register(self, fd: FileDescriptorLike, eventmask: int = ...) -> None: ...
        def modify(self, fd: FileDescriptorLike, eventmask: int) -> None: ...
        def unregister(self, fd: FileDescriptorLike) -> None: ...
        def poll(self, timeout: float | None = None, maxevents: int = -1) -> list[tuple[int, int]]: ...
        @classmethod
        def fromfd(cls, __fd: FileDescriptorLike) -> epoll: ...
    EPOLLERR: int
    EPOLLEXCLUSIVE: int
    EPOLLET: int
    EPOLLHUP: int
    EPOLLIN: int
    EPOLLMSG: int
    EPOLLONESHOT: int
    EPOLLOUT: int
    EPOLLPRI: int
    EPOLLRDBAND: int
    EPOLLRDHUP: int
    EPOLLRDNORM: int
    EPOLLWRBAND: int
    EPOLLWRNORM: int
    EPOLL_RDHUP: int
    EPOLL_CLOEXEC: int

if sys.platform != "linux" and sys.platform != "darwin" and sys.platform != "win32":
    # Solaris only
    class devpoll:
        def close(self) -> None: ...
        closed: bool
        def fileno(self) -> int: ...
        def register(self, fd: FileDescriptorLike, eventmask: int = ...) -> None: ...
        def modify(self, fd: FileDescriptorLike, eventmask: int = ...) -> None: ...
        def unregister(self, fd: FileDescriptorLike) -> None: ...
        def poll(self, timeout: float | None = ...) -> list[tuple[int, int]]: ...
