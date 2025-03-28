from spatial_inventory_rollback.operating_format.rollback_output import (
    RollbackOutput,
)
from spatial_inventory_rollback.procedures.procedure_work_unit import (
    ProcedureWorkUnit,
)


class RollbackProcedure:
    def __init__(self, *args, **kwargs):
        """Interface for rollback procedures. A rollback procedure acts on an
        eligible work unit (determined by the can_rollback method) to roll its
        initial age back to a specified year, optionally adding disturbances.
        """
        pass

    def can_rollback(self, work_unit: ProcedureWorkUnit):  # pragma: no cover
        """Checks if a work unit is eligible to be rolled back to the specified
        year by this procedure.

        Args:
            work_unit (ProcedureWorkUnit): the work unit (unique inventory and
                disturbance sequence) to check rollback eligibility for.
        """
        raise NotImplementedError()

    def rollback(
        self,
        work_unit: ProcedureWorkUnit,
        rollback_year: int,
        rollback_output: RollbackOutput,
    ):  # pragma: no cover
        """Rolls a work unit back to the specified year by calculating a new
        initial age and storing it in age_data, and optionally adding
        disturbance events to disturbance_data.

        Args:
            work_unit (LandscapeWorkUnit): the work unit (unique inventory and
                disturbance sequence) to roll back.
            rollback_year (int): the rollback target year.
            rollback_output (RollbackOutput): stores and writes out new
                inventory and disturbance data generated by the rollback
                procedure.
        """
        raise NotImplementedError()

    def get_procedure_description(
        self, work_unit: ProcedureWorkUnit
    ) -> str:  # pragma: no cover
        """Gets a description of the procedure to be taken on the specified
        work unit

        Args:
            work_unit (ProcedureWorkUnit): ProcedureWorkUnit instance for which
            to return a procedure description

        Returns:
            str: procedure description
        """
        raise NotImplementedError()
