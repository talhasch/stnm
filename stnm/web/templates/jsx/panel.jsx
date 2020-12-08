const Panel = () => {
    const {fetchStatus} = React.useContext(NodeContext);
    const {fetchConfig} = React.useContext(ConfigContext);

    useEffect(() => {
        fetchStatus();
        fetchConfig();
    }, []);

    return (
        <div>
            <NodeInfo/>
            <ConfigInfo/>
            <Mining/>
        </div>
    );
};