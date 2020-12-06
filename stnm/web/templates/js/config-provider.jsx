const ConfigContext = React.createContext();

const CONFIG_INITIAL_STATE = {
    loading: null,
    raw: null,
    object: null,
    inProgress: false
}

const configReducer = (state, action) => {
    switch (action.type) {
        case "FETCH": {
            return {loading: true, config: null}
        }
        case "FETCHED": {
            return {loading: true, raw: action.payload.raw, object: action.payload.object}
        }
        default: {
            return state;
        }
    }
}

const configFetchAct = () => ({
    type: "FETCH",
});

const configFetchedAct = (payload) => ({
    type: "FETCHED",
    payload
});

/*
const configProgressAct = () => ({
    type: "IN_PROGRESS"
});

const configProgressEndAct = () => ({
    type: "IN_PROGRESS_END"
});
*/

const ConfigProvider = ({children}) => {
    const [state, dispatch] = React.useReducer(configReducer, CONFIG_INITIAL_STATE)
    const {loading, raw, object, inProgress} = state;

    const value = {
        loading,
        raw,
        object,
        inProgress,
        fetchConfig: () => {
            dispatch(configFetchAct());
            return fetch("/api/config").then(r => r.json()).then(r => {
                dispatch(configFetchedAct(r));
                return r;
            });
        }
    };

    return (
        <ConfigContext.Provider value={value}>{children}</ConfigContext.Provider>
    )
}