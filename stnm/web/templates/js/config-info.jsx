const ConfigInfo = () => {
    const {loading, raw} = React.useContext(ConfigContext);
    const {status} = React.useContext(NodeContext);

    if (loading === null || !status) {
        return null;
    }

    return <div className="card config-info">
        <h5 className="card-header">Config</h5>
        <div className="card-body">
            {raw !== null && (<pre className="config-pre">
            {raw}
            </pre>)}
        </div>
    </div>
};