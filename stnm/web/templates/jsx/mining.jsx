const Mining = () => {
    const {loading} = React.useContext(ConfigContext);
    const {status} = React.useContext(NodeContext);

    if (loading === null || !status) {
        return null;
    }

    return <Fragment>
        <div className="card config-info">
            <h5 className="card-header">Mining</h5>
            <div className="card-body">
                Coming soon.
            </div>
        </div>
    </Fragment>
};