const NodeInfo = () => {
    return (
        <div className="card node-info">
            <h5 className="card-header">Node Info</h5>
            <div className="card-body">
                <div className="d-flex justify-content-between align-items-center">
                    <h5 className="card-title text-success mb-0">Running</h5>
                    <div>
                        <a href="#" className="btn btn-success btn-sm disabled">Start Node</a>
                        {" "}
                        <a href="#" className="btn btn-danger btn-sm">Stop Node</a>
                    </div>
                </div>
                <table className="table table-sm">
                    <thead>
                    <tr>
                        <th>Lorem</th>
                        <th>Ipsum</th>
                        <th>Dolor</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>sit</td>
                        <td>amet</td>
                        <td>foo</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};