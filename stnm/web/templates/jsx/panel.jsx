const Panel = () => {
    const {fetchStatus} = React.useContext(NodeContext);
    const {fetchConfig} = React.useContext(ConfigContext);

    React.useEffect(() => {
        fetchStatus();
        fetchConfig();
    }, []);

    return (
        <div>
            <NodeInfo/>
            <ConfigInfo/>
        </div>
    );
};