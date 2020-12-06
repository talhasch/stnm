const NodeContext = React.createContext();

const NODE_INITIAL_STATE = {
    loading: null,
    status: null,
    pid: null,
    inProgress: false
}

const nodeReducer = (state, action) => {
    switch (action.type) {
        case "STATUS_FETCH": {
            return {loading: true, status: null, pid: null}
        }
        case "STATUS_FETCHED": {
            if (action.payload.success === true) {
                return {loading: false, status: true, pid: action.payload.pid}
            }

            return {loading: false, status: false, pid: null}
        }
        case "IN_PROGRESS": {
            return {...state, inProgress: true}
        }
        case "IN_PROGRESS_END": {
            return {...state, inProgress: false}
        }
        default:
            return state;
    }
}

const statusFetchAct = () => ({
    type: "STATUS_FETCH",
});

const statusFetchedAct = (payload) => ({
    type: "STATUS_FETCHED",
    payload
});

const progressAct = () => ({
    type: "IN_PROGRESS"
});

const progressEndAct = () => ({
    type: "IN_PROGRESS_END"
});

const NodeProvider = ({children}) => {
    const [state, dispatch] = React.useReducer(nodeReducer, NODE_INITIAL_STATE)
    const {loading, status, pid, inProgress} = state;

    const value = {
        loading,
        status,
        pid,
        inProgress,
        fetchStatus: () => {
            dispatch(statusFetchAct());
            return fetch("/api/status").then(r => r.json()).then(r => {
                dispatch(statusFetchedAct(r));
                return r;
            });
        },
        stopNode: () => {
            dispatch(progressAct());
            return fetch("/api/stop", {
                method: "POST",
            }).then(r => {
                dispatch(progressEndAct());
                return r.json();
            });
        },
        startNode: () => {
            dispatch(progressAct());
            return fetch("/api/start", {
                method: "POST",
            }).then(r => {
                dispatch(progressEndAct());
                return r.json();
            });
        }
    };

    return (
        <NodeContext.Provider value={value}>{children}</NodeContext.Provider>
    )
}