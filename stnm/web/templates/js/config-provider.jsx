const ConfigContext = React.createContext();

const CONFIG_INITIAL_STATE = {
    loading: true,
    data: {}
}

const configReducer = (state, action) => {
    switch (action.type) {
        case 'CONFIG_LOAD':
            return {...state, loading: true}
        case 'CONFIG_LOADED':
            return {...state, data: action.data, loading: false}
        default:
            return state;
    }
}

const configLoadAct = () => ({
    type: 'CONFIG_LOAD',
});

const configLoadedAct = (data) => ({
    type: 'CONFIG_LOADED',
    data
});

const ConfigProvider = ({children}) => {
    const [state, dispatch] = React.useReducer(configReducer, CONFIG_INITIAL_STATE)
    const {data, loading} = state;

    const value = {
        data,
        loading,
        loadConfig: () => {
            dispatch(configLoadAct());
            fetch("/api/config").then(r => r.json()).then(r => {
                dispatch(configLoadedAct(r));
            });
        },
    };

    return (
        <ConfigContext.Provider value={value}>{children}</ConfigContext.Provider>
    )
}