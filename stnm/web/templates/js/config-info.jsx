const ConfigInfo = () => {
    const {loading, config, inProgress, fetchConfig} = React.useContext(ConfigContext);

    React.useEffect(() => {
        if (loading === null) {
            fetchConfig();
        }
    }, []);

    if (loading === null) {
        return null;
    }

    return <div className="card config-info">
        <h5 className="card-header">Config</h5>
        <div className="card-body">
            {config !== null && (<pre className="config-pre">
            {JSON.stringify(config, null, 2)}
            </pre>)}
        </div>
    </div>
};