const NodeInfo = () => {
    const {loading, status, pid, inProgress, fetchStatus, stopNode, startNode} = React.useContext(NodeContext);

    if (loading === null) {
        return null;
    }

    if (loading) {
        return <div className="card node-info">
            <h5 className="card-header">Node Info</h5>
            <div className="card-body">
                <h5 className="card-title mb-0">...</h5>
            </div>
        </div>
    }

    let title = status ? <h5 className="card-title text-success mb-0">Running</h5> : <h5 className="card-title text-danger mb-0">Not running</h5>;
    const btnStart = <button
        onClick={() => {
            startNode().then(() => {
                fetchStatus();
            })
        }}
        className={`btn btn-success btn-sm ${status || inProgress ? "disabled" : ""}`}>Start Node</button>;

    const btnStop = <button
        onClick={() => {
            stopNode().then(() => {
                fetchStatus();
            })
        }} className={`btn btn-danger btn-sm ${!status || inProgress ? "disabled" : ""}`}>Stop Node</button>;

    return (
        <div className="card node-info">
            <h5 className="card-header">Node Info</h5>
            <div className="card-body">
                <div className="d-flex justify-content-between align-items-center">
                    <div>{title}</div>
                    <div>{btnStart}{" "}{btnStop}</div>
                </div>
            </div>
            {status && (
                <div className="card-footer text-muted">
                    Pid: {pid}
                </div>
            )}
        </div>
    );
};